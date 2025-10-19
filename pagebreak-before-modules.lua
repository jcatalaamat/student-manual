-- Pandoc Lua filter to add page breaks before major sections
-- This adds a page break before each MODULE and PART heading

function Header(el)
  -- Check if this is a major section (MODULE or PART)
  local text = pandoc.utils.stringify(el)

  -- Add page break before:
  -- - Any heading that starts with "MODULE"
  -- - Any heading that starts with "PART"
  -- - Level 2 headings that are modules

  if string.match(text, "^MODULE") or
     string.match(text, "^PART") or
     string.match(text, "Module %d+:") then

    -- Create a page break element for Word
    local pagebreak = pandoc.RawBlock('openxml', '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')

    -- Return page break followed by the header
    return {pagebreak, el}
  end

  return el
end
